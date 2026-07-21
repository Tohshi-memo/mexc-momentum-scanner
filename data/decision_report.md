# Decision Report

- generated_at: 2026-07-21T00:31:21.774714+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9133**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9133, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.56% | **-0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +0.51% | **+0.41%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.06% | **-0.04%** |
| LIMIT_BB3S | 2/15 | 13.3% | -0.79% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.82% | **+1.18%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.36% | **+0.95%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.93% | **+0.84%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.18% | **+0.71%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$403.92** / 初期 $100.00 (+303.92%)
- 確定: 3195件 (Win 999 / Loss 1015 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $403.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.65** / 初期 $100.00 (+27.65%)
- 確定: 1094件 (Win 285 / Loss 223 / Flat 586) / skip 1450件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1043 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $127.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.81** / 初期 $100.00 (+1.81%)
- 確定: 330件 (Win 117 / Loss 144 / Flat 69) / pending 6件 / skip 271件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000320 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MVLL/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $101.81

## 6. Latest Market Context

- 更新: 2026-07-21T00:31:15.281205+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=65344.9
- Funnel: target 885 → liquid 168 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +47.67% | $2,648,278.55 |
| HEMI/USDT:USDT | +31.45% | $2,902,143.73 |
| ON/USDT:USDT | +12.59% | $1,800,075.28 |
| BLESS/USDT:USDT | +11.16% | $1,437,756.59 |
| ESPORTS/USDT:USDT | +9.89% | $7,264,226.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +4.38% | +4.19% |
| DEXE/USDT:USDT | below_1h_threshold | +3.11% | +2.92% |
| BLESS/USDT:USDT | below_1h_threshold | +2.39% | +2.20% |
| MONAD/USDT:USDT | below_1h_threshold | +1.31% | +1.13% |
| LDO/USDT:USDT | below_1h_threshold | +1.28% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
