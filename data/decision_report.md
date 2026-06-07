# Decision Report

- generated_at: 2026-06-07T00:58:16.940338+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5916**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=5916, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.21% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +3.90% | **+2.78%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.33% | **+1.13%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.13% | **+0.53%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.38% | **+0.48%** |
| MARKET_LONG | 20/20 | 100.0% | +0.26% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$138.08** / 初期 $100.00 (+38.08%)
- 確定: 1042件 (Win 251 / Loss 320 / Flat 471) / skip 1435件
- 成長率目線: 平均log +0.000310 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $138.08

## 4. Latest Market Context

- 更新: 2026-06-07T00:58:14.463552+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=60775.8
- Funnel: target 771 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +43.69% | $65,741,302.89 |
| SKYAI/USDT:USDT | +34.13% | $30,951,707.69 |
| FIDA/USDT:USDT | +29.15% | $3,444,524.79 |
| BLESS/USDT:USDT | +28.41% | $3,024,969.02 |
| BTW/USDT:USDT | +23.14% | $12,675,286.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +4.38% | +4.50% |
| ALLO/USDT:USDT | below_1h_threshold | +3.29% | +3.42% |
| SIREN/USDT:USDT | below_1h_threshold | +3.15% | +3.27% |
| ZEC/USDT:USDT | below_1h_threshold | +3.03% | +3.15% |
| FIDA/USDT:USDT | below_1h_threshold | +2.69% | +2.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
