# Decision Report

- generated_at: 2026-06-13T17:34:00.869174+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6593**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6593, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.16% | **-1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.03% | **+0.03%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.05% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.08% | **+1.25%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.07% | **+1.14%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.66% | **+0.75%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.12% | **+0.73%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.09% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$165.69** / 初期 $100.00 (+65.69%)
- 確定: 1466件 (Win 392 / Loss 465 / Flat 609) / skip 1688件
- 成長率目線: 平均log +0.000344 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $165.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.72** / 初期 $100.00 (-0.28%)
- 確定: 5件 (Win 1 / Loss 1 / Flat 3) / skip 0件
- 成長率目線: 平均log -0.000561 / 幾何平均 -0.056% per trade / maxDD +0.35%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0320 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $99.72

## 5. Latest Market Context

- 更新: 2026-06-13T17:33:56.539580+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=64086.9
- Funnel: target 770 → liquid 139 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +8.02% | $65,575,963.33 |
| TAO/USDT:USDT | +5.20% | $236,206,562.27 |
| NOT/USDT:USDT | +4.71% | $2,645,943.98 |
| JCT/USDT:USDT | +4.02% | $10,096,226.04 |
| SKYAI/USDT:USDT | +3.93% | $18,548,406.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAO/USDT:USDT | below_1h_threshold | +4.44% | +4.30% |
| AIO/USDT:USDT | below_1h_threshold | +3.98% | +3.84% |
| BTW/USDT:USDT | below_1h_threshold | +2.31% | +2.17% |
| FET/USDT:USDT | below_1h_threshold | +2.25% | +2.11% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +2.19% | +2.05% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
