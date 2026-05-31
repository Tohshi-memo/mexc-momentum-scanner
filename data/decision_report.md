# Decision Report

- generated_at: 2026-05-31T14:14:46.199454+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5195**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5195, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.49% | **-0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.75% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.17% | **+1.73%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.97% | **+1.48%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.40% | **+1.33%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.32% | **+0.73%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.03** / 初期 $100.00 (+27.03%)
- 確定: 830件 (Win 191 / Loss 247 / Flat 392) / skip 926件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.71% 残高後 $127.03

## 4. Latest Market Context

- 更新: 2026-05-31T14:14:43.838530+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=73735.2
- Funnel: target 773 → liquid 117 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +53.44% | $3,913,435.91 |
| PLAY/USDT:USDT | +47.11% | $9,162,161.16 |
| GUN/USDT:USDT | +31.99% | $1,863,728.48 |
| STG/USDT:USDT | +29.73% | $4,573,461.01 |
| TA/USDT:USDT | +21.36% | $2,495,587.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UP/USDT:USDT | below_1h_threshold | +2.90% | +3.04% |
| STG/USDT:USDT | below_1h_threshold | +2.46% | +2.61% |
| GUN/USDT:USDT | below_1h_threshold | +2.25% | +2.40% |
| AIA/USDT:USDT | below_1h_threshold | +1.96% | +2.11% |
| MYX/USDT:USDT | below_1h_threshold | +1.36% | +1.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
