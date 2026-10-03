# Decision Report

- generated_at: 2026-10-03T01:46:24.269887+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16028**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16028, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +2.03% | **+1.52%** |
| LIMIT_BB3S | 5/17 | 29.4% | +1.74% | **+0.51%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.93% | **+0.23%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.16% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.10% | **+1.16%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.16% | **+0.98%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +1.18% | **+0.47%** |
| MARKET_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,326.83** / 初期 $100.00 (+1226.83%)
- 確定: 6133件 (Win 1810 / Loss 1965 / Flat 2358) / skip 6456件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $1,326.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3606件 (Win 1005 / Loss 845 / Flat 1756) / skip 5833件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0416 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4190件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000190 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-03T01:46:12.192811+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=84593.1
- Funnel: target 1099 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +24.70% | $17,341,821.48 |
| VELVET/USDT:USDT | +14.79% | $8,467,607.69 |
| NIGHT/USDT:USDT | +8.14% | $10,444,780.64 |
| SAND/USDT:USDT | +7.31% | $82,098,302.29 |
| ENJ/USDT:USDT | +5.33% | $2,719,760.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ATH/USDT:USDT | below_1h_threshold | +3.19% | +3.21% |
| SYN/USDT:USDT | below_1h_threshold | +2.42% | +2.44% |
| AKE/USDT:USDT | below_1h_threshold | +2.06% | +2.08% |
| SAND/USDT:USDT | below_1h_threshold | +1.64% | +1.66% |
| INJ/USDT:USDT | below_1h_threshold | +1.51% | +1.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
