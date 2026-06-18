# Decision Report

- generated_at: 2026-06-18T10:39:15.542257+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7040**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7040, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.90% | **-1.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | -0.33% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.59% | **+1.35%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.05% | **+1.22%** |
| MARKET_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.19% | **+1.12%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +4.23% | **+1.06%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$215.71** / 初期 $100.00 (+115.71%)
- 確定: 1882件 (Win 530 / Loss 601 / Flat 751) / skip 1719件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $215.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 143件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0643 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T10:39:09.322399+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=63978.9
- Funnel: target 793 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +96.57% | $7,302,016.64 |
| O/USDT:USDT | +75.35% | $4,919,780.96 |
| RE/USDT:USDT | +49.54% | $2,968,147.29 |
| H/USDT:USDT | +33.84% | $34,615,818.49 |
| HOME/USDT:USDT | +33.78% | $2,653,665.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_1h_threshold | +4.30% | +4.61% |
| PORTAL/USDT:USDT | below_1h_threshold | +4.15% | +4.45% |
| MEGA/USDT:USDT | below_1h_threshold | +2.89% | +3.19% |
| LAB/USDT:USDT | below_1h_threshold | +2.11% | +2.41% |
| US/USDT:USDT | below_1h_threshold | +1.93% | +2.23% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
