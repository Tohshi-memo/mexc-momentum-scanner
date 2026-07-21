# Decision Report

- generated_at: 2026-07-21T00:56:20.090165+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9134**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9134, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.16% | **-1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.37% | **+0.31%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.04% | **-0.03%** |
| LIMIT_BB3S | 2/16 | 12.5% | -0.79% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.09% | **+1.46%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.31% | **+1.38%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.18% | **+1.31%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.44% | **+1.29%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +1.43% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$406.47** / 初期 $100.00 (+306.47%)
- 確定: 3196件 (Win 1000 / Loss 1015 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $406.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$128.19** / 初期 $100.00 (+28.19%)
- 確定: 1095件 (Win 286 / Loss 223 / Flat 586) / skip 1450件
- 成長率目線: 平均log +0.000227 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1229 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $128.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定: 331件 (Win 118 / Loss 144 / Flat 69) / pending 6件 / skip 272件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000363 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.99

## 6. Latest Market Context

- 更新: 2026-07-21T00:56:11.044286+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.42% price=65497.0
- Funnel: target 885 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +40.75% | $2,683,281.02 |
| HEMI/USDT:USDT | +23.81% | $2,965,823.47 |
| ON/USDT:USDT | +13.35% | $1,825,640.66 |
| BLESS/USDT:USDT | +9.38% | $1,512,733.89 |
| AKE/USDT:USDT | +8.93% | $23,301,502.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.46% | +4.04% |
| ANSEM/USDT:USDT | below_1h_threshold | +4.38% | +3.96% |
| LDO/USDT:USDT | below_1h_threshold | +2.67% | +2.25% |
| HEMI/USDT:USDT | below_1h_threshold | +1.28% | +0.87% |
| MONAD/USDT:USDT | below_1h_threshold | +1.22% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
