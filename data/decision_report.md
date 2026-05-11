# Decision Report

- generated_at: 2026-05-11T22:32:55.602660+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4074**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4074, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.67% | **+0.30%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.24% | **+0.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.25% | **+2.25%** |
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +6.11% | **+2.04%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.01% | **+1.41%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.81% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 417件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T22:32:52.204325+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=81748.0
- Funnel: target 756 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PENGUIN/USDT:USDT | +19.93% | $2,794,908.30 |
| GIGA/USDT:USDT | +18.66% | $1,352,491.79 |
| USELESS/USDT:USDT | +17.00% | $3,480,780.55 |
| SKYAI/USDT:USDT | +13.26% | $35,849,928.93 |
| RIF/USDT:USDT | +12.58% | $1,303,006.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +3.34% | +3.38% |
| DOGS/USDT:USDT | below_1h_threshold | +3.15% | +3.20% |
| UP/USDT:USDT | below_1h_threshold | +2.72% | +2.77% |
| B/USDT:USDT | below_1h_threshold | +2.12% | +2.16% |
| INJ/USDT:USDT | below_1h_threshold | +1.85% | +1.89% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
