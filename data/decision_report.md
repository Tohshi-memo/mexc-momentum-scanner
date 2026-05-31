# Decision Report

- generated_at: 2026-05-31T18:16:54.281215+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5212**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5212, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.68% | **-1.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.00% | **-0.00%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.78% | **+2.08%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.02% | **+1.96%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.79% | **+1.82%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.95% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.23** / 初期 $100.00 (+29.23%)
- 確定: 847件 (Win 196 / Loss 252 / Flat 399) / skip 926件
- 成長率目線: 平均log +0.000303 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BIANRENSHENG/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $129.23

## 4. Latest Market Context

- 更新: 2026-05-31T18:16:52.038689+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=73607.5
- Funnel: target 773 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +20.96% | $7,909,659.84 |
| BIANRENSHENG/USDT:USDT | +8.41% | $2,507,245.99 |
| PORTAL/USDT:USDT | +8.26% | $11,122,578.01 |
| BILL/USDT:USDT | +3.91% | $5,562,365.90 |
| JUP/USDT:USDT | +3.84% | $1,038,648.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +4.53% | +4.62% |
| UB/USDT:USDT | below_1h_threshold | +2.16% | +2.26% |
| PLAY/USDT:USDT | below_1h_threshold | +1.49% | +1.58% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.14% | +1.24% |
| BSB/USDT:USDT | below_1h_threshold | +0.88% | +0.98% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
