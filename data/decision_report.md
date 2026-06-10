# Decision Report

- generated_at: 2026-06-10T23:15:04.898170+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6277**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6277, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +0.66% | **+0.46%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.69% | **+0.38%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.12% | **+1.56%** |
| ASK_LONG | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.06% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.11% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.95** / 初期 $100.00 (+51.95%)
- 確定: 1263件 (Win 319 / Loss 395 / Flat 549) / skip 1575件
- 成長率目線: 平均log +0.000331 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FOLKS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $151.95

## 4. Latest Market Context

- 更新: 2026-06-10T23:15:01.894480+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=61184.3
- Funnel: target 785 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +89.85% | $37,258,784.98 |
| BEAT/USDT:USDT | +24.02% | $183,861,110.09 |
| STRAX/USDT:USDT | +16.79% | $1,259,611.95 |
| FOLKS/USDT:USDT | +9.35% | $12,309,421.82 |
| POWER/USDT:USDT | +6.84% | $1,465,593.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.77% | +4.05% |
| STRAX/USDT:USDT | below_1h_threshold | +3.18% | +3.45% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.38% | +2.65% |
| VELVET/USDT:USDT | below_1h_threshold | +1.90% | +2.17% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.64% | +1.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
