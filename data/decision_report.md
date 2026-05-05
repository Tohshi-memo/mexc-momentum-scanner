# Decision Report

- generated_at: 2026-05-05T00:57:15.540171+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3281**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.10% / filled 20/20。**
- 全期間 MARKET基準: n=3281, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |
| ASK | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.03% | **+0.83%** |
| LIMIT_BB3S | 3/11 | 27.3% | +2.22% | **+0.60%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.36% | **+0.54%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.66% | **+0.43%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T00:57:13.138894+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=80090.0
- Funnel: target 761 → liquid 205 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +25.84% | $59,919,495.43 |
| FHE/USDT:USDT | +20.35% | $2,714,431.58 |
| TONCOIN/USDT:USDT | +19.94% | $44,956,882.38 |
| PLAY/USDT:USDT | +13.19% | $2,686,555.81 |
| B3/USDT:USDT | +9.96% | $1,150,197.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_relative_strength | +5.00% | +4.67% |
| FHE/USDT:USDT | below_1h_threshold | +4.94% | +4.61% |
| OL/USDT:USDT | below_1h_threshold | +2.00% | +1.67% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.83% | +1.50% |
| ALBSTOCK/USDT:USDT | below_1h_threshold | +1.53% | +1.20% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
