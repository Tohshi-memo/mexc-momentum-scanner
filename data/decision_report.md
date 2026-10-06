# Decision Report

- generated_at: 2026-10-06T10:51:24.479761+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16197**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16197, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +4.36% | **+0.87%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_FIB1618 | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_8PCT | 4/20 | 20.0% | -0.15% | **-0.03%** |
| LIMIT_BB3S | 6/17 | 35.3% | -0.45% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.80% | **+2.80%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.23% | **+1.67%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +2.04% | **+0.92%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.80% | **+0.81%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$120.15** / 初期 $100.00 (+20.15%)
- 確定トレード: 230件 (TP 82 / SL 141 / EXP 7)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.15
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,284.08** / 初期 $100.00 (+1184.08%)
- 確定: 6240件 (Win 1827 / Loss 1995 / Flat 2418) / skip 6518件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,284.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3611件 (Win 1005 / Loss 845 / Flat 1761) / skip 5997件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RLC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4358件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000075 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T10:51:12.225218+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=86181.1
- Funnel: target 1074 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +66.87% | $33,670,192.17 |
| BR/USDT:USDT | +49.44% | $37,704,506.53 |
| US/USDT:USDT | +42.09% | $1,139,356.39 |
| ORCA/USDT:USDT | +28.56% | $3,176,329.24 |
| API3/USDT:USDT | +23.56% | $2,426,513.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RLC/USDT:USDT | below_1h_threshold | +4.71% | +4.43% |
| LONGXIA/USDT:USDT | below_1h_threshold | +4.39% | +4.12% |
| TRB/USDT:USDT | below_1h_threshold | +2.65% | +2.38% |
| ZEC/USDT:USDT | below_1h_threshold | +1.45% | +1.18% |
| VELVET/USDT:USDT | below_1h_threshold | +1.25% | +0.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
