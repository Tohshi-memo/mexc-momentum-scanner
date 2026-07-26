# Decision Report

- generated_at: 2026-07-26T07:16:18.463320+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9561**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9561, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.58% | **+1.03%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.04% | **+0.76%** |
| LIMIT_BB3S | 3/18 | 16.7% | +2.88% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.38% | **+0.36%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.51% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.71% | **+1.71%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.99% | **+1.49%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.28% | **+1.09%** |
| MARKET_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.38% | **+0.83%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$468.72** / 初期 $100.00 (+368.72%)
- 確定: 3389件 (Win 1078 / Loss 1099 / Flat 1212) / skip 2733件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $468.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.15** / 初期 $100.00 (+40.15%)
- 確定: 1214件 (Win 338 / Loss 269 / Flat 607) / skip 1758件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1456 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $140.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.62** / 初期 $100.00 (+9.62%)
- 確定: 604件 (Win 206 / Loss 230 / Flat 168) / pending 3件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000621 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $109.62

## 6. Latest Market Context

- 更新: 2026-07-26T07:16:11.554093+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64396.0
- Funnel: target 898 → liquid 120 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +61.84% | $36,708,873.20 |
| PIEVERSE/USDT:USDT | +45.78% | $1,998,236.32 |
| DIA/USDT:USDT | +37.66% | $2,012,087.24 |
| SHIB/USDT:USDT | +20.58% | $68,345,046.38 |
| LIGHT/USDT:USDT | +14.68% | $1,762,550.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +3.47% | +3.49% |
| KAITO/USDT:USDT | below_1h_threshold | +1.47% | +1.49% |
| BEAT/USDT:USDT | below_1h_threshold | +0.80% | +0.82% |
| SPX/USDT:USDT | below_1h_threshold | +0.53% | +0.55% |
| 1000BONK/USDT:USDT | below_1h_threshold | +0.50% | +0.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
