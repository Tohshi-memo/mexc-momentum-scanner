# Decision Report

- generated_at: 2026-07-16T10:46:36.211526+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8801**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8801, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -1.06% | **-0.11%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.12% | **+1.27%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.40% | **+1.12%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.89% | **+1.04%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.53% | **+0.84%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.17% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$106.87** / 初期 $100.00 (+6.87%)
- 確定トレード: 104件 (TP 38 / SL 64 / EXP 2)
- 最新: ROAM/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.87
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$337.55** / 初期 $100.00 (+237.55%)
- 確定: 2916件 (Win 909 / Loss 945 / Flat 1062) / skip 2446件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZBT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $337.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.27** / 初期 $100.00 (+7.27%)
- 確定: 763件 (Win 175 / Loss 169 / Flat 419) / skip 1449件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0108 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZBT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $107.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.13** / 初期 $100.00 (-1.87%)
- 確定: 72件 (Win 21 / Loss 47 / Flat 4) / pending 1件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000427 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.13

## 6. Latest Market Context

- 更新: 2026-07-16T10:46:28.534659+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=64158.1
- Funnel: target 875 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +19.88% | $5,968,926.21 |
| AKE/USDT:USDT | +16.23% | $44,570,219.69 |
| BANK/USDT:USDT | +15.86% | $2,885,447.12 |
| US/USDT:USDT | +15.42% | $16,324,408.18 |
| CAP/USDT:USDT | +12.53% | $2,974,147.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNHSTOCK/USDT:USDT | below_1h_threshold | +4.77% | +4.62% |
| BANK/USDT:USDT | below_1h_threshold | +4.01% | +3.86% |
| ORDI/USDT:USDT | below_1h_threshold | +2.32% | +2.18% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.26% | +2.11% |
| MYX/USDT:USDT | below_1h_threshold | +2.24% | +2.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
