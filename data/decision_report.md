# Decision Report

- generated_at: 2026-05-05T22:42:45.387102+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3398**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3398, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.84% | **+0.28%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 18/20 | 90.0% | +2.51% | **+2.26%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.78% | **+0.89%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.56% | **+0.55%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.51% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T22:42:42.947468+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.69% price=80802.9
- Funnel: target 759 → liquid 188 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAVIA/USDT:USDT | +22.37% | $1,459,863.63 |
| SWARMS/USDT:USDT | +21.74% | $2,343,281.28 |
| ZEC/USDT:USDT | +19.26% | $587,513,754.61 |
| SMCISTOCK/USDT:USDT | +18.89% | $5,025,007.51 |
| FHE/USDT:USDT | +15.98% | $24,266,590.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AMDSTOCK/USDT:USDT | below_1h_threshold | +3.11% | +3.80% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +1.32% | +2.01% |
| TAO/USDT:USDT | below_1h_threshold | +1.29% | +1.98% |
| VVV/USDT:USDT | below_1h_threshold | +1.19% | +1.88% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.98% | +1.67% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
