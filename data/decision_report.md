# Decision Report

- generated_at: 2026-09-06T08:46:20.361070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13806**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13806, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_BB3S | 4/15 | 26.7% | +0.69% | **+0.18%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.18% | **+0.12%** |
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +5.23% | **+3.14%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +2.27% | **+1.81%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.78% | **+1.33%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.61% | **+1.05%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.54% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$852.00** / 初期 $100.00 (+752.00%)
- 確定: 5112件 (Win 1535 / Loss 1671 / Flat 1906) / skip 5255件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FLOCK/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $852.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$193.89** / 初期 $100.00 (+93.89%)
- 確定: 2551件 (Win 714 / Loss 606 / Flat 1231) / skip 4666件
- 成長率目線: 平均log +0.000260 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0131 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FLOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $193.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.11** / 初期 $100.00 (+20.11%)
- 確定: 2418件 (Win 721 / Loss 919 / Flat 778) / pending 5件 / skip 2855件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000235 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $120.11

## 6. Latest Market Context

- 更新: 2026-09-06T08:46:10.222262+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=79746.0
- Funnel: target 1054 → liquid 125 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1, 4h RSI 65.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +47.12% | $154,368,419.32 |
| FLOCK/USDT:USDT | +41.02% | $1,413,052.40 |
| RAY/USDT:USDT | +30.25% | $3,295,824.62 |
| UAI/USDT:USDT | +20.39% | $13,041,292.08 |
| BASECAT/USDT:USDT | +17.17% | $2,305,292.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.70% | +4.72% |
| CHIP/USDT:USDT | below_1h_threshold | +2.23% | +2.25% |
| JUP/USDT:USDT | below_1h_threshold | +1.25% | +1.28% |
| B/USDT:USDT | below_1h_threshold | +0.96% | +0.98% |
| GRT/USDT:USDT | below_1h_threshold | +0.86% | +0.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
