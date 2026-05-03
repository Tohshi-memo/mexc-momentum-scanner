# Decision Report

- generated_at: 2026-05-03T01:42:08.695122+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3011**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.87% / filled 20/20。**
- 全期間 MARKET基準: n=3011, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.90% | **+0.90%** |
| MARKET | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.51% | **+0.36%** |
| LIMIT_BB3S | 9/17 | 52.9% | +0.64% | **+0.34%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.01% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.08% | **+3.08%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.59% | **+0.88%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.89% | **+0.73%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.35% | **+0.67%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.07% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T01:42:06.693872+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.42% price=78173.1
- Funnel: target 755 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPACE/USDT:USDT | +28.45% | $1,932,379.69 |
| LUNC/USDT:USDT | +19.77% | $34,694,949.52 |
| BIANRENSHENG/USDT:USDT | +14.91% | $1,898,795.84 |
| FHE/USDT:USDT | +14.55% | $2,269,140.57 |
| BABY/USDT:USDT | +13.58% | $1,820,304.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USTC/USDT:USDT | below_1h_threshold | +4.16% | +4.58% |
| LYN/USDT:USDT | below_1h_threshold | +1.44% | +1.85% |
| BSB/USDT:USDT | below_1h_threshold | +1.24% | +1.66% |
| ASTEROID/USDT:USDT | below_1h_threshold | +0.99% | +1.40% |
| LUNC/USDT:USDT | below_1h_threshold | +0.93% | +1.34% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
