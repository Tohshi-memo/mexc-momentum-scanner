# Decision Report

- generated_at: 2026-06-02T20:05:01.184834+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5485**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5485, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.10% | **-2.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.66% | **+0.55%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +3.48% | **+2.78%** |
| ASK_LONG | 20/20 | 100.0% | +2.54% | **+2.54%** |
| MARKET_LONG | 20/20 | 100.0% | +2.38% | **+2.38%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.00% | **+1.30%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.67% | **+1.10%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1070件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T20:04:58.800131+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=67255.1
- Funnel: target 770 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +27.95% | $12,594,587.08 |
| ESPORTS/USDT:USDT | +15.53% | $9,484,937.85 |
| LIT/USDT:USDT | +15.03% | $5,187,193.84 |
| LAB/USDT:USDT | +13.83% | $175,860,752.49 |
| ENA/USDT:USDT | +11.62% | $44,787,337.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +2.71% | +2.75% |
| PANWSTOCK/USDT:USDT | below_1h_threshold | +1.79% | +1.83% |
| NEAR/USDT:USDT | below_1h_threshold | +1.37% | +1.41% |
| XLM/USDT:USDT | below_1h_threshold | +1.22% | +1.26% |
| BILL/USDT:USDT | below_1h_threshold | +1.17% | +1.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
