# Decision Report

- generated_at: 2026-07-25T06:51:24.992543+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9489**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9489, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.96% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.36% | **+0.05%** |
| LIMIT_BB3S | 7/20 | 35.0% | -0.52% | **-0.18%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.26% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.77% | **+1.94%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.03% | **+1.72%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.75% | **+0.88%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.40% | **+0.77%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.87% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 139件 (TP 46 / SL 88 / EXP 5)
- 最新: SYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$423.36** / 初期 $100.00 (+323.36%)
- 確定: 3326件 (Win 1048 / Loss 1077 / Flat 1201) / skip 2724件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $423.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1165件 (Win 312 / Loss 254 / Flat 599) / skip 1735件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0935 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$105.15** / 初期 $100.00 (+5.15%)
- 確定: 540件 (Win 180 / Loss 209 / Flat 151) / pending 6件 / skip 417件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000335 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $105.15

## 6. Latest Market Context

- 更新: 2026-07-25T06:51:14.914206+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=63937.5
- Funnel: target 898 → liquid 164 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +75.49% | $64,311,324.18 |
| EUL/USDT:USDT | +44.15% | $1,998,968.23 |
| AKE/USDT:USDT | +25.87% | $48,142,531.09 |
| ZAMA/USDT:USDT | +20.32% | $4,410,392.70 |
| B2/USDT:USDT | +20.00% | $3,016,551.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +2.99% | +3.07% |
| ZAMA/USDT:USDT | below_1h_threshold | +2.26% | +2.34% |
| UB/USDT:USDT | below_1h_threshold | +1.05% | +1.13% |
| BANK/USDT:USDT | below_1h_threshold | +1.01% | +1.09% |
| AKE/USDT:USDT | below_1h_threshold | +0.96% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
