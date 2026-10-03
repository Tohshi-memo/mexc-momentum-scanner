# Decision Report

- generated_at: 2026-10-03T02:21:30.611077+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16030**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16030, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +2.06% | **+1.55%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.72% | **+0.57%** |
| LIMIT_BB3S | 5/18 | 27.8% | +1.74% | **+0.48%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.22% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.16% | **+0.98%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.01% | **+0.56%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +1.18% | **+0.47%** |
| MARKET_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,320.19** / 初期 $100.00 (+1220.19%)
- 確定: 6135件 (Win 1810 / Loss 1966 / Flat 2359) / skip 6456件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,320.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3606件 (Win 1005 / Loss 845 / Flat 1756) / skip 5835件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0451 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4192件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000181 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-03T02:21:18.693422+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=84624.6
- Funnel: target 1099 → liquid 174 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +44.22% | $17,158,833.30 |
| VELVET/USDT:USDT | +17.67% | $8,642,467.72 |
| SAND/USDT:USDT | +8.63% | $83,822,780.66 |
| NIGHT/USDT:USDT | +7.73% | $10,672,530.39 |
| CT/USDT:USDT | +7.57% | $10,860,584.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAND/USDT:USDT | below_1h_threshold | +3.25% | +3.22% |
| QNT/USDT:USDT | below_1h_threshold | +2.74% | +2.71% |
| CT/USDT:USDT | below_1h_threshold | +2.57% | +2.54% |
| ONE/USDT:USDT | below_1h_threshold | +1.90% | +1.87% |
| ENJ/USDT:USDT | below_1h_threshold | +1.81% | +1.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
