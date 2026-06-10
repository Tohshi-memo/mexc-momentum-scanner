# Decision Report

- generated_at: 2026-06-10T12:09:02.767772+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6213**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6213, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.97% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.70% | **+1.49%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.83% | **+0.37%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| ASK_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.00** / 初期 $100.00 (+49.00%)
- 確定: 1229件 (Win 306 / Loss 384 / Flat 539) / skip 1545件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $149.00

## 4. Latest Market Context

- 更新: 2026-06-10T12:09:00.060430+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=61022.2
- Funnel: target 785 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +50.44% | $13,633,019.84 |
| MAGMA/USDT:USDT | +40.07% | $1,279,037.19 |
| ESPORTS/USDT:USDT | +38.11% | $26,893,102.60 |
| BLEND/USDT:USDT | +32.50% | $1,975,812.70 |
| BTW/USDT:USDT | +27.19% | $31,678,139.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FOLKS/USDT:USDT | below_1h_threshold | +4.10% | +4.07% |
| BTW/USDT:USDT | below_1h_threshold | +1.39% | +1.36% |
| BEAT/USDT:USDT | below_1h_threshold | +1.08% | +1.05% |
| WLFI/USDT:USDT | below_1h_threshold | +0.69% | +0.66% |
| UAI/USDT:USDT | below_1h_threshold | +0.65% | +0.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
