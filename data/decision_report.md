# Decision Report

- generated_at: 2026-07-01T12:31:13.579791+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7983**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=7983, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |
| LIMIT_6PCT | 9/20 | 45.0% | +0.60% | **+0.27%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.18% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.65% | **+1.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.18** / 初期 $100.00 (+160.18%)
- 確定: 2382件 (Win 721 / Loss 789 / Flat 872) / skip 2162件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAIKO/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $260.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.63** / 初期 $100.00 (+6.63%)
- 確定: 503件 (Win 128 / Loss 122 / Flat 253) / skip 891件
- 成長率目線: 平均log +0.000128 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0327 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAIKO/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $106.63

## 5. Latest Market Context

- 更新: 2026-07-01T12:31:06.335822+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=58454.3
- Funnel: target 825 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +108.28% | $11,936,958.64 |
| BAS/USDT:USDT | +36.35% | $2,715,676.96 |
| M/USDT:USDT | +31.97% | $6,457,976.25 |
| BASED/USDT:USDT | +25.36% | $12,782,241.33 |
| ZBT/USDT:USDT | +20.31% | $2,470,594.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +3.42% | +3.66% |
| ZBT/USDT:USDT | below_1h_threshold | +1.62% | +1.85% |
| JASMY/USDT:USDT | below_1h_threshold | +1.06% | +1.30% |
| KAS/USDT:USDT | below_1h_threshold | +0.98% | +1.21% |
| BTW/USDT:USDT | below_1h_threshold | +0.83% | +1.06% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
