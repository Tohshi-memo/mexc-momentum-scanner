# Decision Report

- generated_at: 2026-05-02T21:47:20.691343+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2990**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2990, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/17 | 23.5% | +5.34% | **+1.26%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.44% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.44% | **+1.11%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.29% | **+0.77%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T21:47:17.587182+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.44% price=78757.1
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.4 >= 65=1, 4h RSI 65.9 >= 65=1, 4h RSI 80.7 >= 65=1, 4h RSI 85.0 >= 65=1, 4h RSI 69.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +19.12% | $1,066,448.48 |
| XNY/USDT:USDT | +15.59% | $2,089,919.69 |
| CHILLGUY/USDT:USDT | +14.40% | $1,179,470.93 |
| SPACE/USDT:USDT | +14.33% | $1,748,957.82 |
| LAB/USDT:USDT | +13.57% | $312,237,438.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XNY/USDT:USDT | below_1h_threshold | +4.41% | +3.97% |
| BIO/USDT:USDT | below_1h_threshold | +4.25% | +3.81% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +4.12% | +3.68% |
| BABY/USDT:USDT | below_1h_threshold | +3.48% | +3.05% |
| TRB/USDT:USDT | below_1h_threshold | +3.28% | +2.85% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
