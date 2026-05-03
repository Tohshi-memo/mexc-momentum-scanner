# Decision Report

- generated_at: 2026-05-03T01:52:17.434670+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3014**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.84% / filled 20/20。**
- 全期間 MARKET基準: n=3014, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.87% | **+0.87%** |
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.60% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +2.09% | **+0.42%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.57% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.37% | **+1.78%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.13% | **+0.68%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.35% | **+0.67%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.19% | **+0.64%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.07% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T01:52:15.489838+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=78211.1
- Funnel: target 755 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPACE/USDT:USDT | +34.64% | $2,066,560.61 |
| LUNC/USDT:USDT | +20.14% | $35,398,739.29 |
| BIANRENSHENG/USDT:USDT | +15.50% | $1,939,139.21 |
| BABY/USDT:USDT | +12.82% | $1,848,024.92 |
| FHE/USDT:USDT | +12.29% | $2,289,559.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USTC/USDT:USDT | below_1h_threshold | +4.07% | +4.43% |
| BSB/USDT:USDT | below_1h_threshold | +2.02% | +2.39% |
| LUNC/USDT:USDT | below_1h_threshold | +1.35% | +1.72% |
| ORCA/USDT:USDT | below_1h_threshold | +1.02% | +1.38% |
| LYN/USDT:USDT | below_1h_threshold | +0.93% | +1.30% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
