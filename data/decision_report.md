# Decision Report

- generated_at: 2026-07-16T10:41:17.645068+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8800**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8800, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.13% | **+0.09%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_BB3S | 4/14 | 28.6% | -0.18% | **-0.05%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.40% | **+1.12%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.80% | **+1.08%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.32% | **+0.73%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.96% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$106.87** / 初期 $100.00 (+6.87%)
- 確定トレード: 104件 (TP 38 / SL 64 / EXP 2)
- 最新: ROAM/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.87
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$337.55** / 初期 $100.00 (+237.55%)
- 確定: 2915件 (Win 909 / Loss 945 / Flat 1061) / skip 2446件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $337.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.27** / 初期 $100.00 (+7.27%)
- 確定: 762件 (Win 175 / Loss 169 / Flat 418) / skip 1449件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0110 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $107.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.13** / 初期 $100.00 (-1.87%)
- 確定: 72件 (Win 21 / Loss 47 / Flat 4) / pending 1件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000396 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.13

## 6. Latest Market Context

- 更新: 2026-07-16T10:41:09.904265+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=64163.8
- Funnel: target 875 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +21.34% | $5,963,478.94 |
| US/USDT:USDT | +18.20% | $16,229,767.55 |
| BANK/USDT:USDT | +16.77% | $2,844,893.13 |
| AKE/USDT:USDT | +14.90% | $44,417,355.23 |
| CAP/USDT:USDT | +12.66% | $2,966,024.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +4.94% | +4.79% |
| UNHSTOCK/USDT:USDT | below_1h_threshold | +4.77% | +4.62% |
| ENJ/USDT:USDT | below_1h_threshold | +2.25% | +2.10% |
| BASED/USDT:USDT | below_1h_threshold | +2.19% | +2.04% |
| MYX/USDT:USDT | below_1h_threshold | +2.00% | +1.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
