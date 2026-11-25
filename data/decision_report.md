# Decision Report

- generated_at: 2026-11-25T18:52:32.433978+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19631**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19631, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.58% | **-2.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.62% | **+0.06%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_3PCT_LONG | 6/20 | 30.0% | +3.74% | **+1.12%** |
| LIMIT_2PCT_LONG | 8/20 | 40.0% | +2.24% | **+0.90%** |
| LIMIT_5PCT_LONG | 4/20 | 20.0% | +2.42% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 288件 (TP 105 / SL 175 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,988.31** / 初期 $100.00 (+1888.31%)
- 確定: 7612件 (Win 2191 / Loss 2450 / Flat 2971) / skip 8580件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,988.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.28** / 初期 $100.00 (+367.28%)
- 確定: 5220件 (Win 1389 / Loss 1124 / Flat 2707) / skip 7822件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.09% 残高後 $467.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7805件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-25T18:51:52.164599+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=59754.1
- Funnel: target 1097 → liquid 154 → pre 50 → checked 50 → surge 11 → strict 11
- Surge前reject: below_1h_threshold=38, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOR/USDT:USDT | +22.84% | $1,774,955.56 |
| SOXL/USDT:USDT | +20.45% | $1,860,012,948.09 |
| KORU/USDT:USDT | +15.16% | $97,292,058.58 |
| INTW/USDT:USDT | +14.70% | $1,429,597.56 |
| MVLL/USDT:USDT | +14.51% | $4,872,196.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TQQQ/USDT:USDT | below_relative_strength | +5.24% | +4.94% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +4.29% | +4.00% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +4.26% | +3.96% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +4.12% | +3.82% |
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +4.02% | +3.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
