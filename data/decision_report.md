# Decision Report

- generated_at: 2026-05-01T21:47:14.637415+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2834**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.24% / filled 20/20。**
- 全期間 MARKET基準: n=2834, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.24% | **+1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.68% | **+1.68%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.59% | **+1.51%** |
| MARKET | 20/20 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.34% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.94% | **+0.70%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.98% | **+0.44%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.42% | **+0.25%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.29% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T21:47:12.763919+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=78082.3
- Funnel: target 755 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +23.64% | $7,645,743.95 |
| CHILLGUY/USDT:USDT | +11.59% | $1,014,589.61 |
| BLESS/USDT:USDT | +9.86% | $1,002,127.37 |
| ZEN/USDT:USDT | +8.03% | $8,921,117.97 |
| SNDKSTOCK/USDT:USDT | +7.39% | $6,671,065.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.64% | +3.33% |
| PLAY/USDT:USDT | below_1h_threshold | +3.43% | +3.12% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +2.67% | +2.35% |
| APE/USDT:USDT | below_1h_threshold | +2.61% | +2.30% |
| MEGA/USDT:USDT | below_1h_threshold | +2.18% | +1.86% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
