# Decision Report

- generated_at: 2026-07-28T08:31:35.805839+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9685**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9685, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.92% | **+0.77%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.02% | **+2.02%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.87% | **+1.12%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 148件 (TP 51 / SL 92 / EXP 5)
- 最新: BANK/USDT:USDT TP_HIT PnL +8.00% 残高後 $106.92
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$466.10** / 初期 $100.00 (+366.10%)
- 確定: 3455件 (Win 1091 / Loss 1121 / Flat 1243) / skip 2791件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $466.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1225件 (Win 338 / Loss 275 / Flat 612) / skip 1871件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0345 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.90** / 初期 $100.00 (+7.90%)
- 確定: 705件 (Win 228 / Loss 271 / Flat 206) / pending 4件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000197 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $107.90

## 6. Latest Market Context

- 更新: 2026-07-28T08:31:24.281184+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=63435.7
- Funnel: target 898 → liquid 176 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.6 >= 65=1, 4h RSI 68.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +47.53% | $15,832,654.80 |
| DEXE/USDT:USDT | +33.61% | $15,169,333.84 |
| ON/USDT:USDT | +16.85% | $16,080,491.37 |
| RIF/USDT:USDT | +16.06% | $7,713,680.17 |
| SOONNETWORK/USDT:USDT | +14.42% | $1,742,242.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +1.68% | +1.74% |
| LIT/USDT:USDT | below_1h_threshold | +1.44% | +1.50% |
| SOXS/USDT:USDT | below_1h_threshold | +1.38% | +1.45% |
| SOONNETWORK/USDT:USDT | below_1h_threshold | +1.34% | +1.41% |
| O/USDT:USDT | below_1h_threshold | +1.08% | +1.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
