# Decision Report

- generated_at: 2026-05-05T21:17:25.524933+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3387**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3387, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.73% | **-0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.33% | **+0.70%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.16% | **+0.47%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.42% | **+0.27%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +1.96% | **+1.09%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.48% | **+1.04%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.29% | **+0.92%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.80% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T21:17:23.115736+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=81574.2
- Funnel: target 759 → liquid 186 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.4 >= 65=1, 4h RSI 76.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +44.22% | $18,720,688.89 |
| MAVIA/USDT:USDT | +28.96% | $1,169,408.24 |
| ZEC/USDT:USDT | +19.22% | $537,778,419.01 |
| SWARMS/USDT:USDT | +18.37% | $2,258,004.61 |
| SMCISTOCK/USDT:USDT | +17.49% | $4,378,909.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +4.75% | +4.80% |
| MAVIA/USDT:USDT | below_1h_threshold | +3.27% | +3.32% |
| NIGHT/USDT:USDT | below_1h_threshold | +3.01% | +3.05% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.01% | +2.05% |
| GALA/USDT:USDT | below_1h_threshold | +1.86% | +1.90% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
