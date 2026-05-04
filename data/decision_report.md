# Decision Report

- generated_at: 2026-05-04T21:57:21.461130+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3267**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3267, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.77% | **+0.97%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.86% | **+0.97%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.67% | **+0.83%** |
| LIMIT_BB3S | 4/9 | 44.4% | +0.69% | **+0.31%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.17% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.25% | **+1.00%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.03% | **+0.92%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.08% | **+0.86%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T21:57:18.540502+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.41% price=80223.4
- Funnel: target 759 → liquid 200 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.3 >= 65=1, 4h RSI 82.9 >= 65=1, 4h RSI 90.1 >= 65=1, 4h RSI 66.5 >= 65=1, 4h RSI 80.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +31.46% | $49,062,884.54 |
| PLAY/USDT:USDT | +19.31% | $1,340,643.90 |
| FHE/USDT:USDT | +17.14% | $2,719,333.87 |
| TST/USDT:USDT | +16.90% | $23,258,894.37 |
| TONCOIN/USDT:USDT | +9.78% | $29,800,744.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +3.97% | +3.56% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.82% | +3.41% |
| TIA/USDT:USDT | below_1h_threshold | +3.45% | +3.04% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.84% | +2.43% |
| ZEC/USDT:USDT | below_1h_threshold | +2.68% | +2.27% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
