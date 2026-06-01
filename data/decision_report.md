# Decision Report

- generated_at: 2026-06-01T23:08:02.712374+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5371**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5371, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.50% | **+0.28%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.08% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.08% | **+0.86%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +2.40% | **+0.60%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.46% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 83件 (TP 24 / SL 56 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 1038件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T23:08:00.393975+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=71342.6
- Funnel: target 773 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +25.00% | $6,616,336.88 |
| UB/USDT:USDT | +15.49% | $2,208,115.25 |
| MYX/USDT:USDT | +15.11% | $6,355,550.86 |
| VIC/USDT:USDT | +12.79% | $2,182,489.93 |
| SLX/USDT:USDT | +11.43% | $12,348,006.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +2.37% | +2.42% |
| FET/USDT:USDT | below_1h_threshold | +1.22% | +1.27% |
| ORDI/USDT:USDT | below_1h_threshold | +1.01% | +1.05% |
| PLAY/USDT:USDT | below_1h_threshold | +0.94% | +0.99% |
| GRASS/USDT:USDT | below_1h_threshold | +0.77% | +0.82% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
