# Decision Report

- generated_at: 2026-06-27T03:15:38.681939+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7668**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7668, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.39% | **-1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 4/17 | 23.5% | +0.03% | **+0.01%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.15% | **-0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.67% | **+1.60%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.03% | **+1.36%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.14% | **+0.86%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$235.77** / 初期 $100.00 (+135.77%)
- 確定: 2193件 (Win 656 / Loss 730 / Flat 807) / skip 2036件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGLD/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $235.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.98** / 初期 $100.00 (+7.98%)
- 確定: 399件 (Win 108 / Loss 100 / Flat 191) / skip 680件
- 成長率目線: 平均log +0.000192 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0397 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGLD/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.98

## 5. Latest Market Context

- 更新: 2026-06-27T03:15:34.034203+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=60144.1
- Funnel: target 806 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PUNDIX/USDT:USDT | +43.04% | $4,849,033.30 |
| MYX/USDT:USDT | +26.64% | $3,185,414.60 |
| VELVET/USDT:USDT | +26.45% | $32,910,222.53 |
| SLX/USDT:USDT | +16.16% | $10,919,993.26 |
| ARX/USDT:USDT | +12.73% | $2,603,643.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +3.85% | +4.03% |
| VELVET/USDT:USDT | below_1h_threshold | +3.80% | +3.99% |
| ARX/USDT:USDT | below_1h_threshold | +3.55% | +3.74% |
| G/USDT:USDT | below_1h_threshold | +1.67% | +1.86% |
| JTO/USDT:USDT | below_1h_threshold | +1.32% | +1.50% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
