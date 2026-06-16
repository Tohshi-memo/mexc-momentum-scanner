# Decision Report

- generated_at: 2026-06-16T05:59:49.804620+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6840**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6840, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.52% | **-1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +5.87% | **+0.88%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.25% | **+0.50%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +0.57% | **+0.34%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.23% | **+0.31%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.33% | **+2.33%** |
| ASK_LONG | 20/20 | 100.0% | +2.14% | **+2.14%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.30% | **+0.84%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +2.14% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$181.96** / 初期 $100.00 (+81.96%)
- 確定: 1713件 (Win 446 / Loss 534 / Flat 733) / skip 1688件
- 成長率目線: 平均log +0.000349 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $181.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 95件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0382 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T05:59:44.960216+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=66047.5
- Funnel: target 777 → liquid 159 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.1 >= 65=1, 4h RSI 86.8 >= 65=1, 4h RSI 66.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +59.03% | $3,391,537.90 |
| BSB/USDT:USDT | +30.00% | $20,747,769.99 |
| SPACE/USDT:USDT | +27.77% | $2,379,645.19 |
| ASTEROID/USDT:USDT | +24.64% | $5,985,529.76 |
| VELVET/USDT:USDT | +21.84% | $13,220,610.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +3.53% | +3.18% |
| ASTER/USDT:USDT | below_1h_threshold | +3.15% | +2.79% |
| SPX/USDT:USDT | below_1h_threshold | +3.07% | +2.71% |
| SYN/USDT:USDT | below_1h_threshold | +2.13% | +1.77% |
| AERO/USDT:USDT | below_1h_threshold | +2.10% | +1.74% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
