# Decision Report

- generated_at: 2026-05-31T18:20:59.520202+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5213**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5213, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.00% | **-0.00%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +4.40% | **+2.20%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.61% | **+2.16%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.36% | **+2.02%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.23** / 初期 $100.00 (+29.23%)
- 確定: 848件 (Win 196 / Loss 252 / Flat 400) / skip 926件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $129.23

## 4. Latest Market Context

- 更新: 2026-05-31T18:20:57.476583+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=73600.1
- Funnel: target 773 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +25.22% | $8,135,322.26 |
| BIANRENSHENG/USDT:USDT | +8.92% | $2,593,612.30 |
| PORTAL/USDT:USDT | +6.92% | $11,155,482.14 |
| BILL/USDT:USDT | +4.14% | $5,580,700.84 |
| JUP/USDT:USDT | +3.51% | $1,041,304.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +4.77% | +4.88% |
| STG/USDT:USDT | below_1h_threshold | +4.00% | +4.11% |
| UB/USDT:USDT | below_1h_threshold | +2.24% | +2.34% |
| PLAY/USDT:USDT | below_1h_threshold | +1.32% | +1.43% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.17% | +1.28% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
