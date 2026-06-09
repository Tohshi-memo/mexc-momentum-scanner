# Decision Report

- generated_at: 2026-06-09T16:31:57.040673+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6149**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6149, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.44% | **+1.23%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.22% | **+0.21%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.94% | **+0.19%** |
| ASK | 20/20 | 100.0% | +0.08% | **+0.08%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.10% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.78% | **+1.16%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.42% | **+0.92%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.42% | **+0.85%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.38% | **+0.69%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.93% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$96.14** / 初期 $100.00 (-3.86%)
- 確定トレード: 12件 (TP 1 / SL 10 / EXP 1)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.01** / 初期 $100.00 (+48.01%)
- 確定: 1188件 (Win 297 / Loss 374 / Flat 517) / skip 1522件
- 成長率目線: 平均log +0.000330 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $148.01

## 4. Latest Market Context

- 更新: 2026-06-09T16:31:53.657043+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=61061.4
- Funnel: target 778 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SIREN/USDT:USDT | +13.51% | $9,340,526.23 |
| CHZ/USDT:USDT | +3.20% | $10,436,826.21 |
| H/USDT:USDT | +3.19% | $76,281,613.13 |
| BEAT/USDT:USDT | +3.05% | $124,762,109.04 |
| POL/USDT:USDT | +1.66% | $1,345,088.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.39% | +3.46% |
| CHZ/USDT:USDT | below_1h_threshold | +3.21% | +3.28% |
| BEAT/USDT:USDT | below_1h_threshold | +2.58% | +2.65% |
| POL/USDT:USDT | below_1h_threshold | +1.67% | +1.74% |
| PLAY/USDT:USDT | below_1h_threshold | +1.43% | +1.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
