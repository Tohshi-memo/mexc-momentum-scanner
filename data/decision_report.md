# Decision Report

- generated_at: 2026-06-14T14:52:08.613635+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6672**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.68% / filled 20/20。**
- 全期間 MARKET基準: n=6672, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.68% | **+1.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.68% | **+1.68%** |
| ASK | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.62% | **+0.49%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.49% | **+0.39%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.59% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| ASK_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| MARKET_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.05% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$172.93** / 初期 $100.00 (+72.93%)
- 確定: 1545件 (Win 411 / Loss 489 / Flat 645) / skip 1688件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $172.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 59件 (Win 19 / Loss 12 / Flat 28) / skip 24件
- 成長率目線: 平均log -0.000170 / 幾何平均 -0.017% per trade / maxDD +2.00%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0071 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $99.00

## 5. Latest Market Context

- 更新: 2026-06-14T14:52:04.430229+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.65% price=63867.2
- Funnel: target 770 → liquid 131 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +31.59% | $92,739,448.01 |
| ZKC/USDT:USDT | +29.81% | $1,638,215.78 |
| TRADOOR/USDT:USDT | +29.42% | $8,797,865.17 |
| OPG/USDT:USDT | +23.61% | $1,707,512.33 |
| BANANAS31/USDT:USDT | +20.28% | $1,592,027.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +3.89% | +4.54% |
| BSB/USDT:USDT | below_1h_threshold | +3.48% | +4.12% |
| RIF/USDT:USDT | below_1h_threshold | +3.19% | +3.83% |
| ZKC/USDT:USDT | below_1h_threshold | +3.17% | +3.81% |
| BTW/USDT:USDT | below_1h_threshold | +1.91% | +2.55% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
