# Decision Report

- generated_at: 2026-05-18T18:28:38.668285+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4450**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4450, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.15% | **+0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +0.22% | **+0.17%** |
| MARKET | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.02% | **+0.01%** |
| LIMIT_BB3S | 6/19 | 31.6% | -0.04% | **-0.01%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.09% | **+0.98%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.84% | **+0.55%** |
| ASK_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.86% | **+0.52%** |
| MARKET_LONG | 20/20 | 100.0% | +0.51% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$96.70** / 初期 $100.00 (-3.30%)
- 確定トレード: 54件 (TP 14 / SL 37 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +5.37% 残高後 $96.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.36** / 初期 $100.00 (+20.36%)
- 確定: 447件 (Win 116 / Loss 153 / Flat 178) / skip 564件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $120.36

## 4. Latest Market Context

- 更新: 2026-05-18T18:28:36.704885+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.53% price=76269.7
- Funnel: target 764 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRAC/USDT:USDT | +6.17% | $1,295,011.72 |
| AIGENSYN/USDT:USDT | +3.08% | $4,887,790.81 |
| CHZ/USDT:USDT | +2.51% | $12,561,965.88 |
| USOIL/USDT:USDT | +1.29% | $98,756,065.05 |
| DUSK/USDT:USDT | +1.07% | $1,910,791.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRAC/USDT:USDT | below_1h_threshold | +1.60% | +2.13% |
| USOIL/USDT:USDT | below_1h_threshold | +1.13% | +1.66% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.98% | +1.51% |
| LAB/USDT:USDT | below_1h_threshold | +0.32% | +0.85% |
| DUSK/USDT:USDT | below_1h_threshold | +0.27% | +0.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
