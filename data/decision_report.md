# Decision Report

- generated_at: 2026-06-21T08:35:24.960156+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7298**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.39% / filled 20/20。**
- 全期間 MARKET基準: n=7298, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 3/13 | 23.1% | +1.05% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.67% | **+0.37%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.28% | **+0.34%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.47% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$102.46** / 初期 $100.00 (+2.46%)
- 確定トレード: 25件 (TP 10 / SL 15 / EXP 0)
- 最新: AGT/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$234.09** / 初期 $100.00 (+134.09%)
- 確定: 2027件 (Win 599 / Loss 665 / Flat 763) / skip 1832件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TNSR/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $234.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 398件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T08:35:20.564649+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=63941.0
- Funnel: target 796 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TNSR/USDT:USDT | +64.78% | $5,293,332.37 |
| LAB/USDT:USDT | +21.95% | $22,008,391.21 |
| RESOLV/USDT:USDT | +15.62% | $4,423,851.95 |
| UB/USDT:USDT | +14.49% | $1,237,651.09 |
| MET/USDT:USDT | +13.39% | $1,007,701.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MET/USDT:USDT | below_1h_threshold | +3.01% | +3.37% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.81% | +1.17% |
| ACE/USDT:USDT | below_1h_threshold | +0.71% | +1.06% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.55% | +0.91% |
| RESOLV/USDT:USDT | below_1h_threshold | +0.40% | +0.76% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
