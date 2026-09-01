# Decision Report

- generated_at: 2026-09-01T11:31:29.610737+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13246**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13246, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.16% | **-0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_BB3S | 5/16 | 31.2% | +1.49% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.33% | **+1.06%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.37% | **+0.82%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.73% | **+0.69%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.42% | **+0.43%** |
| MARKET_LONG | 20/20 | 100.0% | +0.41% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$789.79** / 初期 $100.00 (+689.79%)
- 確定: 4882件 (Win 1486 / Loss 1611 / Flat 1785) / skip 4925件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $789.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.98** / 初期 $100.00 (+72.98%)
- 確定: 2225件 (Win 619 / Loss 539 / Flat 1067) / skip 4432件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0264 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $172.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.28** / 初期 $100.00 (+15.28%)
- 確定: 2087件 (Win 610 / Loss 815 / Flat 662) / pending 0件 / skip 2630件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000197 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.28

## 6. Latest Market Context

- 更新: 2026-09-01T11:31:17.892378+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=77925.5
- Funnel: target 1037 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +87.08% | $1,342,269.19 |
| USELESS/USDT:USDT | +32.24% | $26,395,567.61 |
| ARB/USDT:USDT | +31.67% | $86,077,895.19 |
| ONG/USDT:USDT | +19.06% | $5,590,908.23 |
| CRV/USDT:USDT | +15.48% | $6,980,150.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARB/USDT:USDT | below_1h_threshold | +2.50% | +2.58% |
| CRV/USDT:USDT | below_1h_threshold | +1.72% | +1.80% |
| HEMI/USDT:USDT | below_1h_threshold | +1.60% | +1.68% |
| TWT/USDT:USDT | below_1h_threshold | +1.59% | +1.67% |
| O/USDT:USDT | below_1h_threshold | +1.17% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
