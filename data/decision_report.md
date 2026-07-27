# Decision Report

- generated_at: 2026-07-27T06:41:25.874057+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9607**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9607, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 6/20 | 30.0% | +3.58% | **+1.07%** |
| LIMIT_ATR | 19/20 | 95.0% | +0.70% | **+0.66%** |
| LIMIT_9PCT | 6/20 | 30.0% | +1.43% | **+0.43%** |
| LIMIT_8PCT | 6/20 | 30.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/10 | 70.0% | +3.51% | **+2.46%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.65% | **+2.12%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.35% | **+2.12%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.83% | **+1.84%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.29% | **+1.72%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$457.28** / 初期 $100.00 (+357.28%)
- 確定: 3404件 (Win 1080 / Loss 1107 / Flat 1217) / skip 2764件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $457.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1795件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.09** / 初期 $100.00 (+8.09%)
- 確定: 632件 (Win 210 / Loss 241 / Flat 181) / pending 6件 / skip 442件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000206 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.09

## 6. Latest Market Context

- 更新: 2026-07-27T06:41:13.078112+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=65466.9
- Funnel: target 903 → liquid 148 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.9 >= 65=1, 4h RSI 76.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +72.97% | $29,489,331.41 |
| BANK/USDT:USDT | +29.36% | $77,687,513.46 |
| BTW/USDT:USDT | +22.37% | $1,483,348.58 |
| ON/USDT:USDT | +21.67% | $3,812,512.69 |
| DIA/USDT:USDT | +20.81% | $7,896,505.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LDO/USDT:USDT | below_1h_threshold | +2.74% | +2.69% |
| B/USDT:USDT | below_1h_threshold | +1.81% | +1.76% |
| DIA/USDT:USDT | below_1h_threshold | +1.62% | +1.57% |
| NIL/USDT:USDT | below_1h_threshold | +1.59% | +1.54% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.15% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
