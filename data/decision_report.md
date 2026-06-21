# Decision Report

- generated_at: 2026-06-21T12:51:23.805338+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7307**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.64% / filled 20/20。**
- 全期間 MARKET基準: n=7307, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.71% | **+1.71%** |
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 7/20 | 35.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | -0.02% | **-0.02%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | -0.09% | **-0.07%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.61% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$102.46** / 初期 $100.00 (+2.46%)
- 確定トレード: 25件 (TP 10 / SL 15 / EXP 0)
- 最新: AGT/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.60** / 初期 $100.00 (+130.60%)
- 確定: 2030件 (Win 599 / Loss 668 / Flat 763) / skip 1838件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $230.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 407件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0318 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T12:51:18.272080+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=64026.8
- Funnel: target 796 → liquid 136 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TNSR/USDT:USDT | +70.08% | $11,833,952.84 |
| UB/USDT:USDT | +32.38% | $2,009,247.66 |
| LAB/USDT:USDT | +24.22% | $29,875,748.13 |
| BULLA/USDT:USDT | +21.53% | $1,420,780.93 |
| BTR/USDT:USDT | +18.96% | $1,081,755.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +4.63% | +4.83% |
| VELVET/USDT:USDT | below_1h_threshold | +3.88% | +4.07% |
| BASED/USDT:USDT | below_1h_threshold | +2.90% | +3.09% |
| ZRO/USDT:USDT | below_1h_threshold | +1.86% | +2.05% |
| RESOLV/USDT:USDT | below_1h_threshold | +1.60% | +1.79% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
