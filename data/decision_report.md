# Decision Report

- generated_at: 2026-05-26T07:54:21.022271+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4889**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.32% / filled 20/20。**
- 全期間 MARKET基準: n=4889, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.39% | **+1.32%** |
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |
| ASK | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_BB3S | 4/17 | 23.5% | +3.68% | **+0.87%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.01% | **+4.01%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.23% | **+0.25%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.18% | **+0.17%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$97.64** / 初期 $100.00 (-2.36%)
- 確定トレード: 64件 (TP 18 / SL 43 / EXP 3)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.64
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.58** / 初期 $100.00 (+28.58%)
- 確定: 674件 (Win 170 / Loss 214 / Flat 290) / skip 776件
- 成長率目線: 平均log +0.000373 / 幾何平均 +0.037% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DRIFT/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $128.58

## 4. Latest Market Context

- 更新: 2026-05-26T07:54:18.629698+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=76709.9
- Funnel: target 769 → liquid 127 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +83.57% | $2,534,050.74 |
| DRIFT/USDT:USDT | +29.03% | $1,348,463.13 |
| WLD/USDT:USDT | +19.47% | $75,960,300.89 |
| GRASS/USDT:USDT | +9.44% | $9,179,893.24 |
| FET/USDT:USDT | +8.17% | $17,786,958.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHA/USDT:USDT | below_1h_threshold | +4.83% | +5.03% |
| XAN/USDT:USDT | below_1h_threshold | +4.06% | +4.26% |
| RENDER/USDT:USDT | below_1h_threshold | +2.73% | +2.94% |
| LAB/USDT:USDT | below_1h_threshold | +2.13% | +2.34% |
| TIA/USDT:USDT | below_1h_threshold | +1.61% | +1.82% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
