# Decision Report

- generated_at: 2026-07-22T18:31:38.407662+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9306**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9306, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.15% | **-0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +1.57% | **+0.94%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.58% | **+0.55%** |
| LIMIT_BB3S | 3/19 | 15.8% | +2.29% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.25% | **+1.58%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.81% | **+1.09%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.02% | **+0.66%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.75% | **+0.60%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.86% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$105.37** / 初期 $100.00 (+5.37%)
- 確定トレード: 133件 (TP 45 / SL 83 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$429.38** / 初期 $100.00 (+329.38%)
- 確定: 3291件 (Win 1039 / Loss 1060 / Flat 1192) / skip 2576件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $429.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1557件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0194 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.37** / 初期 $100.00 (+1.37%)
- 確定: 426件 (Win 142 / Loss 177 / Flat 107) / pending 2件 / skip 356件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000224 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.37

## 6. Latest Market Context

- 更新: 2026-07-22T18:31:29.753167+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=65839.0
- Funnel: target 890 → liquid 184 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +18.38% | $3,331,345.83 |
| BANK/USDT:USDT | +17.61% | $95,892,597.11 |
| BROCCOLIF3B/USDT:USDT | +11.15% | $1,630,554.11 |
| ON/USDT:USDT | +8.28% | $1,059,647.05 |
| ZAMA/USDT:USDT | +4.10% | $1,996,196.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ON/USDT:USDT | below_1h_threshold | +3.63% | +3.87% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.66% | +1.90% |
| BROCCOLIF3B/USDT:USDT | below_1h_threshold | +1.21% | +1.45% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +0.93% | +1.17% |
| USOIL/USDT:USDT | below_1h_threshold | +0.57% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
