# Decision Report

- generated_at: 2026-05-31T18:40:32.969926+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5214**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5214, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.81% | **-1.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.20% | **+0.16%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +4.02% | **+2.21%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.94% | **+1.77%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.45% | **+1.47%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.26% | **+1.47%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.58** / 初期 $100.00 (+28.58%)
- 確定: 849件 (Win 196 / Loss 253 / Flat 400) / skip 926件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HIVE/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $128.58

## 4. Latest Market Context

- 更新: 2026-05-31T18:40:30.356701+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=73630.8
- Funnel: target 773 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +25.87% | $9,011,213.82 |
| PORTAL/USDT:USDT | +7.50% | $11,330,610.92 |
| HOME/USDT:USDT | +5.94% | $2,101,390.00 |
| UB/USDT:USDT | +4.69% | $6,614,718.16 |
| BIANRENSHENG/USDT:USDT | +4.59% | $2,761,601.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.78% | +4.85% |
| BSB/USDT:USDT | below_1h_threshold | +4.04% | +4.11% |
| UB/USDT:USDT | below_1h_threshold | +3.50% | +3.56% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.58% | +2.64% |
| PLAY/USDT:USDT | below_1h_threshold | +1.23% | +1.29% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
