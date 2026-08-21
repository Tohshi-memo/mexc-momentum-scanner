# Decision Report

- generated_at: 2026-08-21T16:06:20.691286+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12211**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12211, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.75% | **+0.19%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.09% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +4.80% | **+1.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.97% | **+0.82%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +0.34% | **+0.09%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.15% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 189件 (TP 72 / SL 112 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.35** / 初期 $100.00 (+540.35%)
- 確定: 4362件 (Win 1337 / Loss 1434 / Flat 1591) / skip 4410件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BB/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $640.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.94** / 初期 $100.00 (+54.94%)
- 確定: 1827件 (Win 504 / Loss 430 / Flat 893) / skip 3795件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $154.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1867件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000234 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T16:06:10.140447+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=77050.6
- Funnel: target 1018 → liquid 209 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +20.26% | $48,276,275.08 |
| ALIGN/USDT:USDT | +4.31% | $1,004,770.66 |
| LAB/USDT:USDT | +4.06% | $2,451,932.18 |
| BICO/USDT:USDT | +3.93% | $2,343,563.82 |
| US/USDT:USDT | +3.25% | $1,119,418.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.71% | +4.93% |
| ALIGN/USDT:USDT | below_1h_threshold | +4.04% | +4.26% |
| BICO/USDT:USDT | below_1h_threshold | +3.93% | +4.15% |
| US/USDT:USDT | below_1h_threshold | +3.22% | +3.44% |
| CATE/USDT:USDT | below_1h_threshold | +2.39% | +2.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
