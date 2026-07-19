# Decision Report

- generated_at: 2026-07-19T07:11:15.295879+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9008**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9008, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.16% | **-1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.27% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.91% | **+2.76%** |
| MARKET_LONG | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.58% | **+1.55%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.54% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$388.46** / 初期 $100.00 (+288.46%)
- 確定: 3070件 (Win 960 / Loss 977 / Flat 1133) / skip 2499件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $388.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$124.73** / 初期 $100.00 (+24.73%)
- 確定: 969件 (Win 246 / Loss 197 / Flat 526) / skip 1450件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2325 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $124.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.08** / 初期 $100.00 (+0.08%)
- 確定: 211件 (Win 67 / Loss 109 / Flat 35) / pending 4件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000591 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $100.08

## 6. Latest Market Context

- 更新: 2026-07-19T07:11:05.543310+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64662.4
- Funnel: target 885 → liquid 122 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +146.90% | $40,392,784.06 |
| BANK/USDT:USDT | +39.54% | $17,272,108.64 |
| TLM/USDT:USDT | +33.53% | $3,932,369.50 |
| B/USDT:USDT | +29.32% | $38,676,014.84 |
| TAG/USDT:USDT | +23.19% | $3,035,505.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.42% | +4.45% |
| BULLA/USDT:USDT | below_1h_threshold | +2.48% | +2.51% |
| KAITO/USDT:USDT | below_1h_threshold | +1.32% | +1.35% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.16% | +1.19% |
| BILL/USDT:USDT | below_1h_threshold | +1.09% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
