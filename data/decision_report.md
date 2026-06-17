# Decision Report

- generated_at: 2026-06-17T01:59:22.683660+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6894**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6894, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.18% | **-1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.11% | **+0.50%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.09% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.24% | **+1.57%** |
| ASK_LONG | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +0.60% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$191.06** / 初期 $100.00 (+91.06%)
- 確定: 1767件 (Win 471 / Loss 553 / Flat 743) / skip 1688件
- 成長率目線: 平均log +0.000366 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $191.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 167件 (Win 32 / Loss 31 / Flat 104) / skip 138件
- 成長率目線: 平均log -0.000091 / 幾何平均 -0.009% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0600 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $98.49

## 5. Latest Market Context

- 更新: 2026-06-17T01:59:17.299395+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=65895.4
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +38.07% | $2,858,553.93 |
| BLESS/USDT:USDT | +35.03% | $6,697,607.03 |
| H/USDT:USDT | +23.74% | $56,681,690.29 |
| SQD/USDT:USDT | +19.33% | $1,325,219.76 |
| UNI/USDT:USDT | +14.86% | $42,733,852.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.96% | +4.63% |
| LDO/USDT:USDT | below_1h_threshold | +3.18% | +2.85% |
| USELESS/USDT:USDT | below_1h_threshold | +2.49% | +2.16% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.39% | +2.06% |
| ARB/USDT:USDT | below_1h_threshold | +2.39% | +2.06% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
