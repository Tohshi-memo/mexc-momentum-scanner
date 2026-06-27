# Decision Report

- generated_at: 2026-06-27T10:48:02.395249+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7690**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7690, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.94% | **+0.33%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.87% | **+0.09%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.08% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.19% | **+0.87%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.23% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$233.69** / 初期 $100.00 (+133.69%)
- 確定: 2215件 (Win 662 / Loss 738 / Flat 815) / skip 2036件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $233.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.41** / 初期 $100.00 (+7.41%)
- 確定: 421件 (Win 114 / Loss 106 / Flat 201) / skip 680件
- 成長率目線: 平均log +0.000170 / 幾何平均 +0.017% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0440 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $107.41

## 5. Latest Market Context

- 更新: 2026-06-27T10:47:56.789164+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=60372.4
- Funnel: target 806 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +87.11% | $107,003,194.39 |
| MYX/USDT:USDT | +41.95% | $12,540,731.54 |
| SYRUP/USDT:USDT | +21.06% | $2,050,588.04 |
| PUNDIX/USDT:USDT | +17.68% | $6,366,403.72 |
| ARX/USDT:USDT | +13.55% | $2,739,306.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNT/USDT:USDT | below_1h_threshold | +1.56% | +1.59% |
| AAVE/USDT:USDT | below_1h_threshold | +1.49% | +1.52% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.27% | +1.30% |
| XPL/USDT:USDT | below_1h_threshold | +1.22% | +1.25% |
| SYRUP/USDT:USDT | below_1h_threshold | +1.11% | +1.14% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
