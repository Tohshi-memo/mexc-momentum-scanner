# Decision Report

- generated_at: 2026-05-31T00:44:43.725212+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5156**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5156, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.19% | **+0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.64% | **+0.57%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.11% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.82% | **+1.36%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.51% | **+1.36%** |
| ASK_LONG | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.29% | **+1.03%** |
| MARKET_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 78件 (TP 23 / SL 52 / EXP 3)
- 最新: NFP/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.52** / 初期 $100.00 (+23.52%)
- 確定: 794件 (Win 184 / Loss 242 / Flat 368) / skip 923件
- 成長率目線: 平均log +0.000266 / 幾何平均 +0.027% per trade / maxDD +6.10%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_BB3S` SL_HIT account +0.27% 残高後 $123.52

## 4. Latest Market Context

- 更新: 2026-05-31T00:44:41.108527+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=73917.9
- Funnel: target 773 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +41.45% | $6,637,011.71 |
| TA/USDT:USDT | +19.54% | $2,027,571.51 |
| ONDO/USDT:USDT | +13.22% | $34,112,734.05 |
| BIANRENSHENG/USDT:USDT | +13.09% | $1,383,211.16 |
| STG/USDT:USDT | +11.54% | $3,435,164.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXS/USDT:USDT | below_1h_threshold | +4.28% | +4.20% |
| ONDO/USDT:USDT | below_1h_threshold | +3.33% | +3.25% |
| STG/USDT:USDT | below_1h_threshold | +3.23% | +3.15% |
| EDEN/USDT:USDT | below_1h_threshold | +2.97% | +2.88% |
| ID/USDT:USDT | below_1h_threshold | +2.91% | +2.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
