# Decision Report

- generated_at: 2026-09-25T11:11:19.738990+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15522**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15522, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +3.86% | **+1.54%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.76% | **+1.41%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.81% | **+1.36%** |
| LIMIT_6PCT | 4/20 | 20.0% | +6.47% | **+1.29%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.90% | **+1.05%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.96% | **+0.62%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.01% | **+0.46%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.46% | **+0.39%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.37% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$120.08** / 初期 $100.00 (+20.08%)
- 確定トレード: 219件 (TP 79 / SL 135 / EXP 5)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.85% 残高後 $120.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,206.94** / 初期 $100.00 (+1106.94%)
- 確定: 5901件 (Win 1740 / Loss 1890 / Flat 2271) / skip 6182件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.76% 残高後 $1,206.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.32** / 初期 $100.00 (+156.32%)
- 確定: 3455件 (Win 952 / Loss 793 / Flat 1710) / skip 5478件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0567 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $256.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 3171件 (Win 933 / Loss 1255 / Flat 983) / pending 0件 / skip 3823件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XPL/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-25T11:11:10.964032+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=84996.8
- Funnel: target 1069 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARK/USDT:USDT | +33.35% | $1,561,185.20 |
| PHA/USDT:USDT | +23.29% | $2,298,570.92 |
| QNT/USDT:USDT | +18.93% | $15,323,408.29 |
| SYN/USDT:USDT | +16.17% | $3,620,978.38 |
| GRASS/USDT:USDT | +15.95% | $1,134,767.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENA/USDT:USDT | below_1h_threshold | +4.73% | +4.36% |
| JUP/USDT:USDT | below_1h_threshold | +3.16% | +2.78% |
| RAY/USDT:USDT | below_1h_threshold | +2.70% | +2.32% |
| SOL/USDT:USDT | below_1h_threshold | +1.91% | +1.54% |
| GALA/USDT:USDT | below_1h_threshold | +1.64% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
