# Decision Report

- generated_at: 2026-09-01T19:31:32.393730+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13263**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13263, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.11% | **-2.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.96% | **+0.99%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.00% | **+0.90%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.62% | **+0.73%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.62% | **+2.62%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.61% | **+2.09%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.97% | **+1.18%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.87% | **+0.93%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.55% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$809.27** / 初期 $100.00 (+709.27%)
- 確定: 4898件 (Win 1492 / Loss 1614 / Flat 1792) / skip 4926件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.08% 残高後 $809.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.78** / 初期 $100.00 (+75.78%)
- 確定: 2242件 (Win 627 / Loss 539 / Flat 1076) / skip 4432件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0832 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $175.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2646件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000199 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-01T19:31:19.010976+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=77320.4
- Funnel: target 1036 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +12.84% | $5,669,004.37 |
| MAGMA/USDT:USDT | +12.84% | $1,966,074.32 |
| FONE/USDT:USDT | +12.05% | $1,110,961.09 |
| FILECOIN/USDT:USDT | +11.56% | $11,940,655.66 |
| USELESS/USDT:USDT | +10.03% | $36,124,947.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROM/USDT:USDT | below_1h_threshold | +4.82% | +4.56% |
| MAGMA/USDT:USDT | below_1h_threshold | +4.58% | +4.32% |
| FILECOIN/USDT:USDT | below_1h_threshold | +3.65% | +3.39% |
| AR/USDT:USDT | below_1h_threshold | +1.99% | +1.73% |
| ZORA/USDT:USDT | below_1h_threshold | +1.92% | +1.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
