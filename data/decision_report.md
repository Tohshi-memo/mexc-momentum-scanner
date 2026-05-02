# Decision Report

- generated_at: 2026-05-02T21:42:12.520344+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2988**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2988, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/16 | 31.2% | +5.29% | **+1.65%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.25% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.64% | **+1.06%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.61% | **+0.97%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.70% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$102.70** / 初期 $100.00 (+2.70%)
- 確定トレード: 9件 (TP 4 / SL 4 / EXP 1)
- 最新: RAVE/USDT:USDT EXPIRED PnL +5.55% 残高後 $102.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T21:42:07.328867+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.46% price=78774.7
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=44, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.8 >= 65=1, 4h RSI 84.7 >= 65=1, 4h RSI 69.2 >= 65=1, 4h RSI 84.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XNY/USDT:USDT | +18.24% | $2,072,585.93 |
| LAB/USDT:USDT | +17.48% | $309,474,305.92 |
| FHE/USDT:USDT | +16.36% | $1,009,819.13 |
| CHILLGUY/USDT:USDT | +13.70% | $1,174,499.58 |
| SPACE/USDT:USDT | +12.21% | $1,728,406.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_relative_strength | +5.36% | +4.91% |
| BIO/USDT:USDT | below_1h_threshold | +3.90% | +3.44% |
| BABY/USDT:USDT | below_1h_threshold | +3.70% | +3.24% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +3.55% | +3.09% |
| TRB/USDT:USDT | below_1h_threshold | +2.74% | +2.28% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
