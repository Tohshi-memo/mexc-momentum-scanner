# Decision Report

- generated_at: 2026-06-01T00:00:30.261944+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5240**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5240, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.30% | **+0.99%** |
| LIMIT_BB3S | 4/11 | 36.4% | +0.84% | **+0.30%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.00% | **-0.00%** |
| ASK | 20/20 | 100.0% | -0.14% | **-0.14%** |
| LIMIT_10PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +3.58% | **+1.59%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.68% | **+1.52%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.53% | **+1.22%** |
| ASK_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.99** / 初期 $100.00 (+33.99%)
- 確定: 875件 (Win 204 / Loss 260 / Flat 411) / skip 926件
- 成長率目線: 平均log +0.000334 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $133.99

## 4. Latest Market Context

- 更新: 2026-06-01T00:00:27.785182+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=73644.3
- Funnel: target 774 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +109.80% | $19,653,143.41 |
| STG/USDT:USDT | +36.50% | $20,886,802.45 |
| H/USDT:USDT | +19.16% | $12,237,081.32 |
| HOME/USDT:USDT | +16.40% | $3,238,446.23 |
| ZORA/USDT:USDT | +12.47% | $1,634,214.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +1.08% | +1.10% |
| PORTAL/USDT:USDT | below_1h_threshold | +0.92% | +0.94% |
| XLM/USDT:USDT | below_1h_threshold | +0.48% | +0.49% |
| PLAY/USDT:USDT | below_1h_threshold | +0.20% | +0.21% |
| INJ/USDT:USDT | below_1h_threshold | +0.18% | +0.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
