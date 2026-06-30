# Decision Report

- generated_at: 2026-06-30T17:27:40.660978+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7926**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7926, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-2.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.18% | **-2.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.94% | **+0.78%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.11% | **+1.09%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +2.67% | **+0.93%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.64% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$257.84** / 初期 $100.00 (+157.84%)
- 確定: 2355件 (Win 714 / Loss 786 / Flat 855) / skip 2132件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $257.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.52** / 初期 $100.00 (+6.52%)
- 確定: 470件 (Win 125 / Loss 121 / Flat 224) / skip 867件
- 成長率目線: 平均log +0.000134 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0434 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GLM/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.52

## 5. Latest Market Context

- 更新: 2026-06-30T17:27:33.259888+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=58350.8
- Funnel: target 818 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +8.94% | $29,943,365.08 |
| GLM/USDT:USDT | +7.05% | $1,154,621.16 |
| RKLBSTOCK/USDT:USDT | +5.81% | $1,191,529.12 |
| TAIKO/USDT:USDT | +5.00% | $1,018,216.13 |
| H/USDT:USDT | +4.60% | $12,636,173.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVAVSTOCK/USDT:USDT | below_1h_threshold | +2.93% | +3.15% |
| TAIKO/USDT:USDT | below_1h_threshold | +1.66% | +1.88% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +1.10% | +1.32% |
| VELVET/USDT:USDT | below_1h_threshold | +0.92% | +1.14% |
| APE/USDT:USDT | below_1h_threshold | +0.89% | +1.11% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
